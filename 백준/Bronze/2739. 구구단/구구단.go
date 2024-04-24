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
	for x < 10 {
		fmt.Fprintf(writer, "%d * %d = %d\n", n, x, n*x)
		x += 1
	}
}
