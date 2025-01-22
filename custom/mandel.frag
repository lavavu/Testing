//Uniform data
uniform int iterations;
uniform float zoom;
uniform vec2 origin;
uniform sampler2D palette;
uniform vec4 background;

in vec2 vTexCoord;
in vec3 vVertex;
out vec4 colour;

void main()
{
  //Globals
  vec2 z, c;
  colour = background;
  vec2 coord = origin + vTexCoord * (1.0/zoom);

  //Mandelbrot set default
  z = vec2(0,0);
  c = coord;

  //Iterate the fractal formula
  int i;
  for (i=0; i < iterations; i++)
  {
    //z(n+1) =
    z = vec2(z.x*z.x - z.y*z.y, z.x*z.y + z.y*z.x) + c;
    //Check bailout condition
    if (dot(z,z) > 100)
      break;
  }

  colour = texture(palette, vec2(float(i) / float(iterations), 0.0));
}
