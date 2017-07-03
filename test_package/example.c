#include <png.h>
#include <stdio.h>

int main(int argc, char** argv)
{
  fprintf(stderr, "   Compiled with libpng %s; using libpng %s.\n",
    PNG_LIBPNG_VER_STRING, png_libpng_ver);

	return 0;
}
