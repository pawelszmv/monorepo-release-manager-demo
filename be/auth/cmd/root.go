package cmd

import (
    "github.com/spf13/cobra"
    "os"
)

var rootCmd = &cobra.Command{
    Use:   "auth",
    Short: "Authentication service",
    Long:  `A simple authentication service that provides login and logout functionalities.`,
    Run: func(cmd *cobra.Command, args []string) {
        // Default action when no subcommand is provided
        cmd.Help()
    },
}

func Execute() {
    if err := rootCmd.Execute(); err != nil {
        os.Exit(1)
    }
}

func init() {
    // Define any persistent flags here
    rootCmd.PersistentFlags().StringP("config", "c", "", "config file (default is $HOME/.auth.yaml")
}