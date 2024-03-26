import paramiko
def run_ssh_command(hostname, username, password, command):
    # Create an SSH client instance
    client = paramiko.SSHClient()
    # Automatically add the server's host key
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    try:
        # Connect to the server
        client.connect(hostname, username=username, password=password)
        # Run the command
        stdin, stdout, stderr = client.exec_command(command)
        # Read the output
        output = stdout.read().decode("utf-8")
        # Print the output
        print(output)
    except Exception as e:
        print(f"Error: {e}")
    finally:
        # Close the SSH connection
        client.close()

# Example usage
if __name__ == "__main__":
    hostname ="192.168.1.66"
    username = ("vvirtualbox")
    password = "Root@123"
    command = ("ls -l")
    run_ssh_command(hostname, username, password, command)