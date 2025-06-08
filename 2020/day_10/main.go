package main

import (
	"flag"
	"fmt"
    "encoding/json"
	"strings"
	"os"
    "strconv"
    "sort"
	// "regexp"
)

func main() {
	var part int
	var in_f string
	flag.IntVar(&part, "part", 1, "part 1 or 2")
	flag.StringVar(&in_f, "in_f", "", "input filename")
	flag.Parse()
	
	in_lines, _ := os.ReadFile(in_f)

	var ans int
	if part == 1 {
		ans = Part1(string(in_lines))
	} else {
		ans = Part2(string(in_lines))
	}
	fmt.Printf("ans: %v\n", ans)
}

func print(idk any) {
	jsonBytes, _ := json.MarshalIndent(idk, "", "   ")
	fmt.Println(string(jsonBytes))
}

func ParseInput(in_lines string) []int {
	lines_split := strings.Split(in_lines, "\r\n")
	ret_slc := make([]int, len(lines_split))
	for i, char := range lines_split {
		ret_slc[i], _ = strconv.Atoi(char)
	}
	return ret_slc
}

func Part1(in_lines string) int {
	lines := ParseInput(in_lines)
	lines = append(lines, 0)
	sort.Slice(lines, func(i, j int) bool {
		return lines[i] < lines[j]
	})
	lines = append(lines, lines[len(lines)-1] + 3)
	deltas := map[int]int{}
	var j int
	for i := range lines[:len(lines)-1] {
		j = i+1
		delta := lines[j] - lines[i]
		if _, ok := deltas[delta]; !ok {
			deltas[delta] = 0
		}
		deltas[delta]++
	}
	ret := 1
	for i := range deltas {
		ret *= deltas[i]
	}
	return ret
}

var qty_paths int = 0

func CheckValidPaths(lines, path []int) {
	// print(lines)
	if len(lines) == 1 {
		qty_paths += 1
		// print(path)
	}
	for i := range lines {
		// fmt.Printf("qty_paths: %v ,i: %v\n", qty_paths, i)
		if i == 0 {
			continue
		} else if lines[i] - lines[0] <= 3 {
			CheckValidPaths(lines[i:], append(path, lines[i]))
		}
	}
}

func Part2(in_lines string) int {
	lines := ParseInput(in_lines)
	sort.Slice(lines, func(i, j int) bool {
		return lines[i] < lines[j]
	})
	path := make([]int, 0)
	CheckValidPaths(lines, path)

	return qty_paths
}