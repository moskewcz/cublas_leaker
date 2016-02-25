#include "cublas_v2.h"
int main() {
  cublasHandle_t handle;
  cublasCreate(&handle);
  cublasDestroy(handle);
  return 0;
}
