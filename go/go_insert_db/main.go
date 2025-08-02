package main

import (
	"bufio"
	"encoding/json"
	"fmt"
	"kenya6111/hc_practice/go/go_insert_db/config"
	"kenya6111/hc_practice/go/go_insert_db/handlers"
	"log"
	"net/http"
	"os"

	"github.com/gorilla/mux"
	_ "github.com/lib/pq"
)

type User struct {
	Age   int       `json:"age"`
	Name  string    `json:"name"`
	Role  string    `json:"role"`
}

type Log struct {
	User  User   `json:"user"`
	Dist  string `json:"dist"`
	Level string `json:"level"`
	Msg   string `json:"msg"`
	Src   string `json:"src"`
	Time  string `json:"time"`
}

func main(){
	db, err := config.SetupDB()
	if err != nil{
		log.Fatal(err)
	}
	defer db.Close()

	args := os.Args
	if len(args) != 2 {
		fmt.Println("引数の数が間違っています")
		os.Exit(1)
	}
	f2, err := os.OpenFile(args[1],os.O_RDONLY, 0644)
	if err != nil {
		fmt.Println("err ", err)
		os.Exit(1)
	}
	defer f2.Close()

	scanner := bufio.NewScanner(f2)
	tx, err := db.Begin()
	if err != nil {
    	log.Fatal(err)
	}

    for scanner.Scan() {

		var log Log
		if err := json.Unmarshal(scanner.Bytes(), &log); err != nil{
			fmt.Printf("JSON parse error: %v\n", err)
			tx.Rollback()
			os.Exit(1)
		}

		sqlStatement := `INSERT INTO users (age, name, role) VALUES ($1, $2, $3)`
		_, err = tx.Exec(sqlStatement,log.User.Age, log.User.Name, log.User.Role)
		if err != nil {
			tx.Rollback()
			fmt.Println(err)
			os.Exit(1)
		}
		fmt.Println(scanner.Text())
    }
	if err := scanner.Err(); err != nil {
		fmt.Println("ファイル読み取り中のエラー:", err)
		tx.Rollback()
		os.Exit(1)
	}

	if err := tx.Commit(); err != nil {
		log.Fatal(err)
	}

	r := mux.NewRouter()
	r.HandleFunc("/hello",handlers.HelloHandler).Methods(http.MethodGet)

	log.Println("server start at port 8091")
	log.Fatal(http.ListenAndServe(":8091",r))
}