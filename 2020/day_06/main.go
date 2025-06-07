package main

import (
	"flag"
	"fmt"
	"log"
	"os"
	"strings"
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
	var part int
	var in_f string
	flag.IntVar(&part, "part", 1, "part 1 or 2")
	flag.StringVar(&in_f, "in_f", "", "input filename")
	flag.Parse()
	// fmt.Println("Running part", part)
	// fmt.Println("Running part", in_f)
    // fmt.Println("tail:", flag.Args())
	
	var in_lines string = MyReadFile(in_f)
	// fmt.Println(in_lines)
	var ans int
	if part == 1 {
		ans = Part1(in_lines)
	} else {
		ans = Part2(in_lines)
	}
	fmt.Printf("ans: %v\n", ans)
}

func Part1(in_lines string) int {
	ret := 0
	for _, line := range strings.Split(in_lines, "\n\n") {
		oneLine := strings.ReplaceAll(line, "\n", "")

		charSet := map[string]bool{}
		for _, char := range strings.Split(oneLine, "") {
			charSet[char] = true
		}
		
		ret += len(charSet)
	}

	return ret
}

func Part2(in_lines string) int {
	ret := 0
	for _, line := range strings.Split(in_lines, "\n\n") {
		each_form := strings.Split(line, "\n")
		charSet := map[string]bool{}

		for _, char := range each_form[:1][0] {
			charSet[string(char)] = true
		}

		if len(each_form) > 0 {
			for _, each_tester := range each_form[1:] {
				for key, _ := range charSet {
					if !(strings.Contains(each_tester, key)) {
						delete(charSet, key)
					}
				}
			}
		}	
		ret += len(charSet)
	}

	return ret
}