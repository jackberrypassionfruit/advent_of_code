package main

import (
	"flag"
	"fmt"
	"log"
	"os"
	"strings"
	"regexp"
    "strconv"
    "encoding/json"
)

func MyReadFile(file string) string {
    content, err := os.ReadFile(file)
    if err != nil { log.Fatal(err) }
	return string(content)
}

func main() {
	var part int
	var in_f string
	flag.IntVar(&part, "part", 1, "part 1 or 2")
	flag.StringVar(&in_f, "in_f", "", "input filename")
	flag.Parse()
	
	var in_lines string = MyReadFile(in_f)

	var ans int
	if part == 1 {
		ans = Part1(in_lines)
	} else {
		ans = Part2(in_lines)
	}
	fmt.Printf("ans: %v\n", ans)
}

func ParseInput(in_lines string) map[string]map[string]int {
	re_container := "^([a-z ]+) bags contain"
	r1, _ := regexp.Compile(re_container)
	re_contained := "(\\d+) ([a-z ]+) bag(?:s)?"
	r2, _ := regexp.Compile(re_contained)
	graph := map[string]map[string]int{}

	for _, line := range strings.Split(in_lines, "\n") {
		container_match := r1.FindStringSubmatch(line)
		container := container_match[1]
		contained_match := r2.FindAllString(line, -1)
		graph[container] = map[string]int{}
		for _, bag := range contained_match {
			bag_match := r2.FindStringSubmatch(bag)
			qty, color := bag_match[1], bag_match[2]
			qty_int, _ := strconv.Atoi(qty)
			graph[container][color] = qty_int
		}
	}
	return graph
}

func dfsShinyGoldBag(graph map[string]map[string]int, entry string) bool {
	_, has_shiny_gold := graph[entry]["shiny gold"]
	if has_shiny_gold {
		return true
	}
	for subBag := range graph[entry] {
		if dfsShinyGoldBag(graph, subBag) {
			return true
		}
	}
	return false
}

func Part1(in_lines string) int {
	graph := ParseInput(in_lines)
    // jsonBytes, _ := json.MarshalIndent(graph, "", "   ")
	// fmt.Println(string(jsonBytes))
	
	ret_slc := map[string]bool{}
	for bag := range graph {
		if dfsShinyGoldBag(graph, bag) {
			ret_slc[bag] = true
		}
	}
	jsonBytes, _ := json.MarshalIndent(ret_slc, "", "   ")
	fmt.Println(string(jsonBytes))


	return len(ret_slc)
}

func countBags(graph map[string]map[string]int, entry string) int {
	subBags, _ := graph[entry]
	if len(subBags) == 0 { return 1 }
	ret := 1
	for bag := range subBags {
		qty_bags, _ := graph[entry][bag]
		fmt.Printf("bag: %v, qty_bags: %v\n", bag, qty_bags)
		ret += qty_bags * countBags(graph, bag)
		// fmt.Println(qty_bags)
	}

	return ret
}

func Part2(in_lines string) int {
	graph := ParseInput(in_lines)
    jsonBytes, _ := json.MarshalIndent(graph, "", "   ")
	fmt.Println(string(jsonBytes))
	countedBags := countBags(graph, "shiny gold")
	// returns 1 more bag than correct answer, idk why
	return countedBags
}