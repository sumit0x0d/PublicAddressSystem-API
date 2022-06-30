package main

import (
	"fmt"
	"net/http"
)

type ZoneResponse struct {
	IP     string
	Port   string
	Status string
}

func zone(w http.ResponseWriter, r *http.Request) {
	ip := r.URL.Query().Get("ip")
	port := r.URL.Query().Get("port")
	turn := r.URL.Query().Get("turn")
	client(ip, port, turn)
	_, err := w.Write([]byte("successful"))
	if err != nil {
		panic(err)
	}
}

func speaker(w http.ResponseWriter, r *http.Request) {
	values := r.URL.Query()
	if !(values.Has("status")) {
		fmt.Println("suzz")
	}
}

func microphone(w http.ResponseWriter, r *http.Request) {
	values := r.URL.Query()
	if !(values.Has("status")) {
		// _, err := w.Write()
		// if err != nil {
		// 	panic(err)
		// }
	}
}
