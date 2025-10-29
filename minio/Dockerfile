FROM rockylinux:9 AS builder

ARG MINIO_RELEASE
WORKDIR /src

RUN dnf install -y git golang && dnf clean all

RUN git clone --branch $MINIO_RELEASE --depth 1 https://github.com/minio/minio.git /src/minio \
    && cd /src/minio \
    && GOOS=linux GOARCH=amd64 go build -o bin/minio ./cmd

FROM rockylinux:9
WORKDIR /build

ARG MINIO_RELEASE

RUN dnf install -y rpm-build sed && dnf clean all

COPY --from=builder /src/minio/bin/minio /build/
COPY minio.spec minio.service minio.default /build/

RUN RPM_VERSION=$(echo ${MINIO_RELEASE} \
                   | sed -E 's/^RELEASE\.//; s/T//; s/-//g; s/Z//') \
    && RPM_VERSION="${RPM_VERSION}.0.0" \
    && sed -i "s/^Version:.*/Version: ${RPM_VERSION}/" minio.spec

RUN mkdir -p rpmbuild/{BUILD,RPMS,SOURCES,SPECS,SRPMS} \
    && cp /build/minio rpmbuild/SOURCES/ \
    && cp /build/minio.spec rpmbuild/SPECS/ \
    && cp /build/minio.service rpmbuild/SOURCES/ \
    && cp /build/minio.default rpmbuild/SOURCES/

RUN rpmbuild --define "_topdir $(pwd)/rpmbuild" -bb rpmbuild/SPECS/minio.spec
