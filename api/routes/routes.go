package routes

import (
	"github.com/ManoVikram/AI-Fine-Tuning/api/handlers"
	"github.com/ManoVikram/AI-Fine-Tuning/api/services"
	"github.com/gin-gonic/gin"
)

func RegisterRoutes(server *gin.Engine, services *services.Services) {
	server.POST("/api/ask", handlers.AskHandler(services))
}
