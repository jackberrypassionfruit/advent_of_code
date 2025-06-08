package main

import (
	"flag"
	"fmt"
	"os"
	"strings"
	"regexp"
    "strconv"
    "encoding/json"
)

type step struct {
	Instruction string
	Value int
}

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

func ParseInput(in_lines string) []step {
	lines_slice := strings.Split(in_lines, "\n")
	var steps []step
	for _, line := range lines_slice {
		re_instruction := "^(nop|acc|jmp) ([+-])(\\d+)$"
		r, _ := regexp.Compile(re_instruction)
		rg := r.FindStringSubmatch(line)
		instruction, sign, val := rg[1], rg[2], rg[3]
		var signed_val int
		if valint, _ := strconv.Atoi(val); sign == "+" {
			signed_val = valint
		} else {
			signed_val = -1 * valint
		}

		steps = append(steps, step{
			Instruction: instruction,
			Value: signed_val,
		})
	}
	return steps
}

func Accumulate(steps []step) (int, bool) {
	i := 0
	beenHereBefore := map[int]bool{}
	acc := 0
	for {
		switch this_val := steps[i].Value; steps[i].Instruction {
			case "nop":
				i++
			case "acc":
				i++
				acc += this_val
			case "jmp":
				i += this_val
		}
		_, ok := beenHereBefore[i]
		if ok { 
			return acc, false
		} else if i == len(steps) {
			return acc, true
		}
		beenHereBefore[i] = true
	}
}

func Part1(in_lines string) int {
	steps := ParseInput(in_lines)
	// print(steps)
	accumulated, _ := Accumulate(steps)
	return accumulated
}


func Part2(in_lines string) int {
	steps := ParseInput(in_lines)
	var accumulated int
	var revert string
	for j := range steps {
		switch steps[j].Instruction {
		case "nop":
			revert = "nop"
			steps[j].Instruction = "jmp"
		case "jmp":
			revert = "jmp"
			steps[j].Instruction = "nop"
		default:
			continue
		}
		
		accumulated, finished := Accumulate(steps)
		if finished {
			return accumulated
		}
		steps[j].Instruction = revert
	}
	return accumulated
}