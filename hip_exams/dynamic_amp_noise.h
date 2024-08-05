float smoothstep(float edge0; float edge1; float x)
{
    float t = clamp((x - edge0) / (edge1 - edge0), 0.0, 1.0);
    return t * t * (3.0 - 2.0 * t);
}

float dynamic_amp_noise(float px, py, f, sx, sy, ox, oy, time; int turb; float rough, atten, amp)
{
    float x = px * f - ox + sx * time;
    float y = py * f - oy + sy * time;
    float z = 12.3456789;
    vector pos = set(x, y, z);
    vector noise;
    noise = onoise(pos, turb, rough, atten);
    noise = noise * amp;

    float noise_x = getcomp(noise, 0);
    noise_x = smoothstep(-1, 1, noise_x);

    return noise_x;
}

float px = @P.x;
float py = @P.y;
float f = ch("frequency");
float sx = ch("speed_x");
float sy = ch("speed_y");
float ox = ch("offset_x");
float oy = ch("offset_y");
float time = @Time;
int turb = chi("turbulence");
float rough = ch("roughness");
float atten = ch("attenuation");
float amp = ch("amplitude");

int start_frame = $FSTART;
int end_frame = $FEND;
float fps = $FPS;
float duration = (end_frame - start_frame + 1) / fps;

float norm_time = time / duration;
float looped_time = norm_time - floor(norm_time); 

@Cd += dynamic_amp_noise(px, py, f, sx, sy, ox, oy, looped_time * duration, turb, rough, atten, amp);
