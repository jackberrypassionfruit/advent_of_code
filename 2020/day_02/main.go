package main

import (
	"fmt"
	"log"
	"os"
	"strings"
	"strconv"
)

func MyReadFile(file string) string {
    content, err := os.ReadFile(file)
    if err != nil {
        log.Fatal(err)
    }
    // fmt.Println(string(content))
	return string(content)
}

func main() {
	filename := os.Args[1]
	input_text := MyReadFile(filename)
	// fmt.Printf(input_text)

	pass_cunt := 0
	for _, line := range strings.Split(input_text, "\n") {
		// fmt.Println(line)
		ls := strings.Split(line, " ")
		splt, char, txt := ls[0], strings.TrimRight(ls[1], ":"), ls[2]
		splt_splt := strings.Split(splt, "-")
		min, _ := strconv.Atoi(splt_splt[0])
		max, _ := strconv.Atoi(splt_splt[1])
		
		char_cunt := 0
		for _, bit := range strings.Split(txt, "") {
			// fmt.Println(bit)
			if bit == char { char_cunt += 1 }
		}
		
		if min <= char_cunt && char_cunt <= max {
			pass_cunt++
		}

		// fmt.Printf("min=%v, max=%v, char=%v, txt=%v, char_cunt=%v\n", min, max, char, txt, char_cunt)
	}
	fmt.Printf("pass_cunt=%v\n", pass_cunt)

}