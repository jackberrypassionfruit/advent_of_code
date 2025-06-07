package main

import (
    "fmt"
	"log"
    "os"
	"io"
	"time"
    "reflect"
	"runtime"
	"strings"
	"strconv"
)

type fn func(file string) string

func GetFunctionName(i interface{}) string {
    return runtime.FuncForPC(reflect.ValueOf(i).Pointer()).Name()
}

func TimeIt(call_me fn, arg string) string {
	start := time.Now()
	ret := call_me(arg)
	ex_time := time.Now().Sub(start)
	fmt.Printf("Ran %v in %q\n", GetFunctionName(call_me), ex_time)
	return ret
}

func MyReadFile(file string) string {
    content, err := os.ReadFile(file)
    if err != nil {
        log.Fatal(err)
    }
    // fmt.Println(string(content))
	return string(content)
}

func MyOpen(file string) string {
    // open input file
    fi, err := os.Open(file)
    if err != nil {
        panic(err)
    }
    // close fi on exit and check for its returned error
    defer func() {
        if err := fi.Close(); err != nil {
            panic(err)
        }
    }()

	// make a buffer to keep chunks that are read
    buf := make([]byte, 2048)
    for {
        // read a chunk
        n, err := fi.Read(buf)
        if err != nil && err != io.EOF {
            panic(err)
        }
		// fmt.Printf("line: %v", string(buf[:n]))
        if n == 0 {
            break
        }
    }
	return string(buf)
}
func FindPair(filename string) string {
	input_text := MyReadFile(filename)
	splt := strings.Split(input_text, "\n")
	for i, ni := range splt {
		for j, nj := range splt {
			for k, nk := range splt {
				niint, _ := strconv.Atoi(ni)
				njint, _ := strconv.Atoi(nj)
				nkint, _ := strconv.Atoi(nk)

				if i != j && j != k && i != k && niint + njint + nkint == 2020 {
					prod := niint * njint * nkint
					// fmt.Printf("fuck yeah: %v * %v = %v", ni, nj, prod)
					fmt.Println(prod)
					return ""
				}
			}
		}
	}
	return ""
}

func main() {
	filename := "input.txt"
	// input_text := TimeIt(MyOpen, filename)
	// input_text := TimeIt(MyReadFile, filename)
	// MyReadFile(filename)
	// MyOpen(filename)

	// fmt.Printf("%v\n", input_text)
	// for _, word := range strings.Split(input_text, "\n") {
	// 	fmt.Printf("%v ", word)
	// }

	// TimeIt(FindPair, filename)
	FindPair(filename)
}