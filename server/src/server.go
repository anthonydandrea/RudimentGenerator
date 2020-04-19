package main

import (
        "fmt"
        "regexp"
        "os/exec"
        "net/http"
        "math/rand"
        "strconv"
        "os"
)

type RudimentOptions struct {
        numBeats int

}

func getRudimentOptionsCLIString(options RudimentOptions) string {
        return "--numBeats " + strconv.Itoa(options.numBeats)
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
                        options.numBeats, err = strconv.Atoi(v[0])
                        fmt.Println(err)
                case "oldFileName":
                        fileToDelete = v[0]
                }
            }

                fileprefix := fmt.Sprintf("%f", rand.Float64())
                fileoptions := getRudimentOptionsCLIString(options)
                fmt.Println(fileprefix + " " + fileoptions)

                out := exec.Command("./generate_rudiment.sh", fileprefix, fileoptions).Run()
                
                if out != nil {
                        fmt.Printf("%s", out)
                    }

                fmt.Fprintf(w, fileprefix+".pdf")

                fmt.Println("remove static/rudiments/"+fileToDelete)
                match, _ := regexp.MatchString("^0.[0-9]*.pdf", fileToDelete)
                if !match {
                        fmt.Println("Bad string input")
                } else {
                        exec.Command("rm", "static/rudiments/"+fileToDelete).Run()
                }
                
    }

func main() {
        http.Handle("/", http.FileServer(http.Dir("./static")))
        http.HandleFunc("/rudiment", getRudiment)

        port, exists := os.LookupEnv("PORT")
        if exists {
                http.ListenAndServe(":"+port, nil)
           } else {
                http.ListenAndServe(":3001", nil)
           }
        
}