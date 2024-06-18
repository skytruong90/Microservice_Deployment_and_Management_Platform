import subprocess

def kubectl_apply(filename):
    """Apply a Kubernetes configuration using kubectl."""
    try:
        subprocess.run(["kubectl", "apply", "-f", filename], check=True)
        print(f"Deployment of {filename} succeeded.")
    except subprocess.CalledProcessError as e:
        print(f"Deployment of {filename} failed: {str(e)}")

def main():
    """Main function to deploy Kubernetes configurations."""
    # List of Kubernetes YAML files to deploy
    configs = ["service.yaml", "deployment.yaml"]
    
    for config in configs:
        kubectl_apply(config)

if __name__ == "__main__":
    main()
