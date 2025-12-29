package handlers

import (
	"fmt"
	"net/http"

	"github.com/ManoVikram/AI-Fine-Tuning/api/models"
	pb "github.com/ManoVikram/AI-Fine-Tuning/api/proto"
	"github.com/ManoVikram/AI-Fine-Tuning/api/services"
	"github.com/gin-gonic/gin"
)

func AskHandler(services *services.Services) gin.HandlerFunc {
	return func(c *gin.Context) {
		// Step 1 - Get the request body and unmarshal it
		var request models.GeneralServiceRequest

		if err := c.ShouldBindJSON(&request); err != nil {
			c.JSON(http.StatusBadRequest, gin.H{"error": fmt.Sprintf("Invalid request body: %v", err.Error())})
			return
		}

		// Step 2 - Convert the request to protobuf format (gRPC request)
		grpcRequest := &pb.GeneralServiceRequest{
			Query: request.Query,
		}

		// Step 3 - Call the gRPC method to get an answer
		grpcResponse, err := services.Client.Ask(c.Request.Context(), grpcRequest)
		if err != nil {
			c.JSON(http.StatusInternalServerError, gin.H{"error": fmt.Sprintf("Unable to process the query at the moment: %v", err.Error())})
			return
		}

		// Step 4 - Convert the gRPC response to API response
		response := models.GeneralServiceResponse{
			Answer: grpcResponse.Answer,
		}

		// Step 5 - Return the response
		c.JSON(http.StatusOK, response)
	}
}
