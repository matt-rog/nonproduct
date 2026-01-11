package main

import (
    "log"
    "gateway/pkg/db"
)

func main() {
    log.Print("Nonproduct Gateway Server has started")

    _, err := db.StartDB()
    if err != nil {
        log.Printf("Error starting the database %v", err)
    }
}
