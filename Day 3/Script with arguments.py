import subprocess

service = input("Please enter your service: ")

result = subprocess.run(
    ["systemctl", "status", service],
    capture_output=True,
    text=True
)

print(result.stdout)