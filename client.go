package main

import (
	"bytes"
	"encoding/binary"
	"fmt"
	"io/ioutil"
	"net/http"

	"github.com/gordonklaus/portaudio"
)

const sampleRate = 44100
const seconds = 2

func client(ip string, port string, turn string) string {
	err := portaudio.Initialize()
	if err != nil {
		return turn
	}
	defer portaudio.Terminate()
	numInputChannels := 0
	numOutputChannels := 1
	data := make([]float32, sampleRate*seconds)
	framesPerBuffer := len(data)
	args := func(out []float32) {
		url := fmt.Sprintf("http://%s:%s/audio", ip, port)
		resp, err := http.Get(url)
		if err != nil {
			return turn
		}
		b, _ := ioutil.ReadAll(resp.Body)
		r := bytes.NewReader(b)
		order := binary.BigEndian
		binary.Read(r, order, &data)
		for i := range out {
			out[i] = data[i]
		}
	}
	stream, err := portaudio.OpenDefaultStream(numInputChannels, numOutputChannels, sampleRate, framesPerBuffer, args)
	if err != nil {
		return turn
	}
	err = stream.Start()
	if err != nil {
		return turn
	}
	// time.Sleep(time.Second * 40)
	// err = stream.Stop()
	// if err != nil {
	// 	panic(err)
	// }
	defer stream.Close()
}
