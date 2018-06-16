## Example app showing docker usage

```bash
docker build -t npentrel/docker-them-all-v1
docker run --name static-site -d -p 8888:9000 npentrel/docker-them-all-v1
```
