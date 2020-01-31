package main

import (
	"log"
	"net/smtp"
	"strings"
	"fmt"
)

type loginAuth struct {
    username, password string
}

func LoginAuth(username, password string) smtp.Auth {
    return &loginAuth{username, password}
}

func (a *loginAuth) Start(server *smtp.ServerInfo) (string, []byte, error) {
    return "LOGIN", nil, nil
}

func (a *loginAuth) Next(fromServer []byte, more bool) ([]byte, error) {
    command := string(fromServer)
    command = strings.TrimSpace(command)
    command = strings.TrimSuffix(command, ":")
    command = strings.ToLower(command)

    if more {
        if (command == "username") {
            return []byte(fmt.Sprintf("%s", a.username)), nil
        } else if (command == "password") {
            return []byte(fmt.Sprintf("%s", a.password)), nil
        } else {
            return nil, fmt.Errorf("unexpected server challenge: %s", command)
        }
    }
    return nil, nil
}

func main() {
	err := smtp.SendMail("smtp.outlook.com:587", LoginAuth("duy.huynh@knorex.com", "pass"), "duy.huynh@knorex.com", []string{"duuuuuuuuy@gmail.com"}, []byte("Hello"))
	if err != nil {
		log.Fatal(err)
	}
}
