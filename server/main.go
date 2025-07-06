package main

import (
	"github.com/gin-gonic/gin"

	"github.com/jzho987/whatami/server/usage"
)

func main() {
	e := gin.Default()
	e.GET("/usage/pc", usage.GetPCUsage)
}
