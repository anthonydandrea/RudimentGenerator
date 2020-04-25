package main

import (
	"fmt"
	"math/rand"
	"net/http"
	"os"
	"os/exec"
	"regexp"
	"strconv"
)

type RudimentOptions struct {
	beats   int
	accents int
	rights  int
	buzzes  int
	diddles int
	flams   int
	cheeses int

	triplets   bool
	sixteenths bool
	fivelets   bool
}

func getRudimentOptionsCLIString(options RudimentOptions) string {
	cli_str := " --beats " + strconv.Itoa(options.beats) +
		" --accents " + strconv.Itoa(options.accents) +
		" --rights " + strconv.Itoa(options.rights) +
		" --buzzes " + strconv.Itoa(options.buzzes) +
		" --diddles " + strconv.Itoa(options.diddles) +
		" --flams " + strconv.Itoa(options.flams) +
		" --cheeses " + strconv.Itoa(options.cheeses)

	if options.triplets {
		cli_str += " --triplets "
	}

	if options.sixteenths {
		cli_str += " --sixteenths "
	}

	if options.fivelets {
		cli_str += " --fivelets "
	}

	return cli_str
}

func getRudiment(w http.ResponseWriter, r *http.Request) {

	if r.Method != "GET" {
		return
	}

	var options RudimentOptions
	var err error
	var fileToDelete string

	for k, v := range r.URL.Query() {
		fmt.Printf("%s: %s\n", k, v)
		switch k {
		case "beats":
			options.beats, err = strconv.Atoi(v[0])
			fmt.Println(err)
		case "accents":
			options.accents, err = strconv.Atoi(v[0])
			fmt.Println(err)
		case "rights":
			options.rights, err = strconv.Atoi(v[0])
			fmt.Println(err)
		case "buzzes":
			options.buzzes, err = strconv.Atoi(v[0])
			fmt.Println(err)
		case "diddles":
			options.diddles, err = strconv.Atoi(v[0])
			fmt.Println(err)
		case "flams":
			options.flams, err = strconv.Atoi(v[0])
			fmt.Println(err)
		case "cheeses":
			options.cheeses, err = strconv.Atoi(v[0])
			fmt.Println(err)
		case "triplets":
			options.triplets, err = strconv.ParseBool(v[0])
			fmt.Println(err)
		case "sixteenths":
			options.sixteenths, err = strconv.ParseBool(v[0])
			fmt.Println(err)
		case "fivelets":
			options.fivelets, err = strconv.ParseBool(v[0])
			fmt.Println(err)
		case "oldFileName":
			fileToDelete = v[0]
		}
	}

	fmt.Println(options)

	fileprefix := fmt.Sprintf("%f", rand.Float64())
	fileoptions := getRudimentOptionsCLIString(options)
	fmt.Println(fileprefix + " " + fileoptions)

	out := exec.Command("./generate_rudiment.sh", fileprefix, fileoptions).Run()

	if out != nil {
		fmt.Printf("%s", out)
	}

	fmt.Fprintf(w, fileprefix+".pdf")

	fmt.Println("remove static/rudiments/" + fileToDelete)
	match, _ := regexp.MatchString("^0.[0-9]*.pdf", fileToDelete)
	if !match {
		fmt.Println("Bad string input")
	} else {
		exec.Command("rm", "static/rudiments/"+fileToDelete).Run()
	}

}

func main() {
	path, err := os.Getwd()
	if err != nil {
		fmt.Println(err)
	}
	fmt.Println(path)
	http.Handle("/", http.FileServer(http.Dir("./static")))
	http.HandleFunc("/rudiment", getRudiment)

	port, exists := os.LookupEnv("PORT")
	if exists {
		http.ListenAndServe(":"+port, nil)
	} else {
		http.ListenAndServe(":3001", nil)
	}

}
