package usage

import (
	"log/slog"
	"net/http"
	"strconv"

	"github.com/gin-gonic/gin"
)

func GetPCUsage(ctx *gin.Context) {
	startTimeQuery := ctx.Query("startTime")
	if len(startTimeQuery) == 0 {
		slog.Error("start time query does not exist")
		ctx.Status(http.StatusBadRequest)
		return
	}
	startTime, parseErr := strconv.ParseInt(startTimeQuery, 10, 64)
	if parseErr != nil {
		slog.Error("failed to parse start time query when getting pc usage")
		ctx.Status(http.StatusBadRequest)
		return
	}

	endTimeQuery := ctx.Query("endTime")
	if len(endTimeQuery) == 0 {
		slog.Error("end time query does not exist")
		ctx.Status(http.StatusBadRequest)
		return
	}
	endTime, parseErr := strconv.ParseInt(endTimeQuery, 10, 64)
	if parseErr != nil {
		slog.Error("failed to parse start time query when getting pc usage")
		ctx.Status(http.StatusBadRequest)
		return
	}

	ctx.Status(http.StatusOK)
}
