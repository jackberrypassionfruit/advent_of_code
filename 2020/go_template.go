package main

import (
	"flag"
	"fmt"
	"os"
	// "strings"
	// "regexp"
    // "strconv"
    // "encoding/json"
)


func main() {
	var part int
	var in_f string
	flag.IntVar(&part, "part", 1, "part 1 or 2")
	flag.StringVar(&in_f, "in_f", "", "input filename")
	flag.Parse()
	
	in_lines, _ := os.ReadFile(in_f)
	// fmt.Println(string(in_lines))
	var ans int
	if part == 1 {
		ans = Part1(string(in_lines))
	} else {
		ans = Part2(string(in_lines))
	}
	fmt.Printf("ans: %v\n", ans)
}


func Part1(in_lines string) int {
	fmt.Print(in_lines)
	return 0
}


func Part2(in_lines string) int {
	fmt.Print(in_lines)
	return 0
}