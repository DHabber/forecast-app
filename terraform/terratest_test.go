package test

import (
	"testing"
	"time"
	"context"

	"github.com/gruntwork-io/terratest/modules/terraform"
)

func TestTerraformBasicExample(t *testing.T) {
	// Increase the timeout to 60 minutes (3600 seconds)
	testTimeout := 60 * time.Minute
	t.Parallel()

	terraformOptions := terraform.WithDefaultRetryableErrors(t, &terraform.Options{
		// Set the path to the Terraform code that will be tested.
		TerraformDir: "terraform-eks",
	})

	// Create a context with a timeout
	ctx, cancel := context.WithTimeout(context.Background(), testTimeout)
	defer cancel()

	// Run the test function in a Goroutine with the custom context
	var testErr error
	go func() {
		// Ensure the test function is executed before canceling the context
		defer terraform.Destroy(t, terraformOptions)
		terraform.InitAndApply(t, terraformOptions)
		// Your test assertions go here
	}()

	// Wait for the test to complete or the timeout to be reached
	select {
	case <-ctx.Done():
		if ctx.Err() == context.DeadlineExceeded {
			// Handle the timeout error
			t.Errorf("Test exceeded the allowed timeout of %v", testTimeout)
		}
	case <-time.After(testTimeout + 1*time.Minute):
		// Give a small buffer for cleanup in case of a failure
	}

	if testErr != nil {
		t.Fatalf("Test failed: %v", testErr)
	}
}

//execute with: go test -v -timeout 60m terratest_test.go
