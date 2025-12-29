package main

import (
	"fmt"
	"log"
	"os"

	pb "github.com/ManoVikram/AI-Fine-Tuning/api/proto"
	"github.com/ManoVikram/AI-Fine-Tuning/api/routes"
	"github.com/ManoVikram/AI-Fine-Tuning/api/services"
	"github.com/gin-gonic/gin"
	"github.com/joho/godotenv"
	"google.golang.org/grpc"
	"google.golang.org/grpc/credentials/insecure"
)

func main() {
	// Step 0 - Load the environment variables
	godotenv.Load()
	grpcServer := os.Getenv("GRPC_SERVER")
	grpcServerPort := os.Getenv("GRPC_SERVER_PORT")
	grpcServerAddress := grpcServer + ":" + grpcServerPort

	// Step 1 - Connect to the gRPC server
	connection, err := grpc.NewClient(grpcServerAddress, grpc.WithTransportCredentials(insecure.NewCredentials()))
	if err != nil {
		log.Fatalf("%s", fmt.Sprintf("Failed to connect to gRPC server at %s: %v", grpcServer, err.Error()))
		return
	}

	// Step 2 - Create a gRPC service client
	client := pb.NewGeneralServiceClient(connection)

	// Step 3 - Initialize the services with the gRPC client
	services := &services.Services{
		Client: client,
	}

	// Step 4 - Initialize the set up the Gin server
	server := gin.Default()

	// Step 5 - Register the routes
	routes.RegisterRoutes(server, services)
}
