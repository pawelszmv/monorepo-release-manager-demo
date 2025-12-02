package main

import (
    "github.com/spf13/cobra"
    "log"
    "os"
)

var Version = "dev" // overwritten at build time with -ldflags

func main() {
    var rootCmd = &cobra.Command{
        Use:     "auth",
        Short:   "Authentication service",
        Long:    `A simple authentication service built with Go and Cobra.`,
        Version: Version,
    }

    // Add subcommands here
    rootCmd.AddCommand(serveCmd)

    if err := rootCmd.Execute(); err != nil {
        log.Println(err)
        os.Exit(1)
    }
}