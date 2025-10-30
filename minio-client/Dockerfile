FROM rockylinux:9 AS builder

ARG MC_RELEASE
WORKDIR /src

RUN dnf install -y git golang && dnf clean all

RUN git clone --branch $MC_RELEASE --depth 1 https://github.com/minio/mc.git /src/mc \
    && cd /src/mc \
    && CGO_ENABLED=0 GOOS=linux GOARCH=amd64 go build -o bin/mc .

FROM rockylinux:9
WORKDIR /build

ARG MC_RELEASE

RUN dnf install -y rpm-build sed && dnf clean all

COPY --from=builder /src/mc/bin/mc /build/mc
COPY minio-client.spec /build/

RUN RPM_VERSION=$(echo ${MC_RELEASE} \
                   | sed -E 's/^RELEASE\.//; s/T//; s/-//g; s/Z//') \
    && RPM_VERSION="${RPM_VERSION}.0.0" \
    && sed -i "s/^Version:.*/Version: ${RPM_VERSION}/" minio-client.spec

RUN mkdir -p rpmbuild/{BUILD,RPMS,SOURCES,SPECS,SRPMS} \
    && cp /build/mc rpmbuild/SOURCES/ \
    && cp /build/minio-client.spec rpmbuild/SPECS/

RUN rpmbuild --define "_topdir $(pwd)/rpmbuild" -bb rpmbuild/SPECS/minio-client.spec
