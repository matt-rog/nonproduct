package main

import (
	"gateway/internal/db"
	"log"
)

func main() {
	log.Print("Nonproduct Gateway Server has started")

	_, err := db.StartDB()
	if err != nil {
		log.Printf("Error starting the database %v", err)
	}
}
