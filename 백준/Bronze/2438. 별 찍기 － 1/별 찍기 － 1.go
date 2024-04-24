package main

import (
	"bufio"
	"fmt"
	"os"
)

func main() {
	var reader *bufio.Reader = bufio.NewReader(os.Stdin)
	var writer *bufio.Writer = bufio.NewWriter(os.Stdout)

	defer writer.Flush()

	var n int

	fmt.Fscanln(reader, &n)

	x := 1
	for x <= n {
		y := 1
		for y <= x {
			fmt.Fprint(writer, "*")
			y++
		}
		x += 1
		fmt.Fprintln(writer)
	}
}
