## Beginner Level
1. What does CI/CD Stands for in DevOps
2. What is DevOps?
3. What are the key benefits of DevOps
4. What are the key components of DevOps
5. Name some popular DevOps tools
6. What is version control, and why is it
7. What's the difference between Git and GitHub
8. What is infrastructure as Code(IaC)
9. What is pipeline in DevOps
  A pipeline is an automated sequence of steps -- form coding to deployment that ensures continuous delivery. It includes stages like build, test, deploy, and monitor.
  pipelines make sure software move seemlessly from development to production with minimal manual effort

10. **Merge Conflicts**

    Occur when two branches modify the same line of a file differently. Git stops the merge and requires manual intervention to decide which code to keep.

11. **GitHub Action**

    a continuous integration and continuous delivery (CI/CD) and automation platform built directly into **GitHub**. It allows you to automate software development workflows like building, testing, and deploying your code right from your repository.

## Intermediate Questions

### 1. What is Docker, and why is it used

​	Docker is a containerisation platform that packages an application and its dependencies into a portable unit called a container. It ensures consistency across environments -- meaning software runs the same way on a developer's laptop as it does on production servers. Docker improves efficiency, speeds up deployment, and simplifies scaling.

### 2. What's the difference between containers and virtual machines(VMs)

​	VMs virtualize hardware, each running its own OS, making them heavy and slow to start. Containers on the other hand, share the host OS kernel, making the lightweight, and faster. Containers are ideal for micro-services and scalable cloud environments.

### 3. What is Kubernetes

​	Kubernetes (K8s) is an open-source platform that automates the deployment, scaling, and management of containerzed application. It handles container scheduling, networking, storage, and self-healing ensuring application remain resilient even if nodes fail

### 4. What are CI/CD tools commonly used in DevOps?

​	Popular CI/CD tools include jenkins, GitLab CI, CircleCI and Azure DevOps these tools automate build, test and deployment pipelines, helping teams detect errors early, reduce manual work and ensure faster releases.

### 5. What is Configuration Mangement

​	Configuration management ensures consistency across environments by automating system setup maintenance. Tools like Ansible, Chef and Puppet help manage configuration, deploy updates, and maintain infrastructure at scale.

### 6. Explain the concepts of "Shift-left testing"

​	Shift-left testing means starting testing earlier in the software lifecycle rather than waiting until the end. This helps detect bugs sooner, reduces costs, and ensures higher software quality, It aligns well with the DevOps culture of continuous feedback.

### 7. What is the role of monitoring in DevOps

​	Monitoring ensures systems are healthy and performing well. Tools like Prometheus and Grafana tack metrics such as CPU usage, uptime, latency, and error rates. continuous monitoring helps teams detect and fix issues proactively.

### 8. What is a Microservice Architecture

Microservices architecture breaks applications into small, independent services that can be developed, deployed, and scaled separately. This approach improves flexibility, reduces downtime, and allows different teams to work on different components simultaneously.

### 9. What is a blue-green deployment

​	A blue-green deployment used tow identical environments - Blue(current production) and Green(new Version). The new release is deployed to Green, tested, and once stable, traffic is switched from Blue to Green. This minimizes downtime and ensures smooth rollouts.

## 10. What are the best practices for CI/CD pipelines

- Keep pipelines automated and version-controlled
- Include automated testing at each stage
- Use consistent environments (containers)\
- Add security scanning.
- Enable rollback stategies
- Monitor pipeline performance and errors.

## Advanced Questions

### 1. What is DevSecOps

​	DevSecOps integrates security practices into every phase of the DevOps pipeline. It ensures that security isn't just an afterthought but a shared responsibility. Automated
vulnerability scans, code reviews, and compliance checks are built into CI/CD workflows.

### 2. How to you handle secrets in a DevOps pipeline?

​	Secrets like API keys or credentials should never be hardcoded. Tools like HashiCorp Vault, AWS Secrets Manager, or Kubernetes Secrets encrypt and store them securely. Environment variables or secret management integrations are used to access them
safely.

### 3. How does Terraform differs form Ansible

​	Terraform is an Infrastructure as Code (laC) tool primarily used for provisioning
infrastructure creating servers, databases, and networks. Ansible, however, focuses on
configuration management — installing packages, updating servers, and maintaining
systems post-deployment.

### 4. What are the key metrics to measure DevOps success

**Key metrics include:**

- Deployment Frequency: How often releases happen
- Lead Time for Changes: Time from code commit to production.
- MTTR (Mean Time to Recovery): Time to fix production failures.
- Change Failure Rate: Percentage of deployments causing issues.

### 5. How do you ensure zero-downtime deployment

​	Zero-downtime deployments use strategies like blue-green, canary, or rolling updates. Traffic is gradually shifted to new versions, and rollbacks are automatic if errors occur ensuring users never experience interruptions.

### 6. What is Chaos Engineering

​	Chaos engineering is a proactive approach to system reliability. It involves intentionally breaking components (like shutting down servers) to test how systems recover. This helps teams identify weaknesses and build resilient architectures.

### 7. How do containers improve CI/CD process

​	Containers create consistent environments across development, testing , and production. They reduce compatibility issues, enable faster builds, and simplify rollbacks. Containers make CI/CD pipelines more predictable and efficient.

### 8. How does cloud computing integrate with DevOps

​	Cloud platforms like AWS, Azure, and GCP provide scalable infrastructure, APIs, and managed services that support automation and CI/CD. DevOps teams can spin up
environments quickly, reducing dependency on physical servers.

### 9. What is your approach to troubleshooting a failed deployment

​	Start by reviewing pipeline logs and monitoring alerts to locate the root cause. Check configuration files, recent commits, or infrastructure changes. Roll back if necessary, apply the fix in a test environment, retest, and redeploy. Post-mortem analysis should follow to prevent recurrence.





