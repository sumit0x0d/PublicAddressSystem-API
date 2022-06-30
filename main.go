package main

import (
	"net/http"
)

func main() {
	go server()
	http.HandleFunc("/zone", zone)
	http.HandleFunc("/speaker", speaker)
	http.HandleFunc("/microphone", microphone)
	err := http.ListenAndServe(":8080", nil)
	if err != nil {
		panic(err)
	}
	// go server()
	// time.Sleep(1000)
	// go client()
	// for {

	// }
}
