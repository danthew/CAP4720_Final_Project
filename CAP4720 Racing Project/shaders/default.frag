#version 330 core

layout (location  = 0) out vec4 fragColor;

in vec2 uv_0;
in vec3 normal;
in vec3 fragPos;
in vec4 shadowCoord;

struct Light {
    vec3 position;
    vec3 Ia;
    vec3 Id;
    vec3 Is;
};

uniform Light light;
uniform sampler2D u_texture_0;
uniform vec3 camPos;
uniform sampler2DShadow shadowMap;

float getShadow(){
    // hardware-level function to check if pixel is in shadow
    float shadow = textureProj(shadowMap, shadowCoord);
    return shadow;
}

vec3 getLight(vec3 color){
    vec3 Normal = normalize(normal);

    // ambient light
    vec3 ambient = light.Ia;

    // diffuse light
    vec3 lightDir = normalize(light.position - fragPos);
    float diff = max(0, dot(lightDir, Normal));
    vec3 diffuse = diff * light.Id;

    // specular light
    vec3 viewDir = normalize(camPos - fragPos);
    vec3 reflectDir = reflect(-lightDir, Normal);
    // 32 determines the shininess of the object
    float spec = pow(max(dot(viewDir, reflectDir),  0), 32);
    vec3 specular = spec * light.Is;

    // shadow
    float shadow = getShadow();

    return color * (ambient + (diffuse + specular) * shadow);
}

void main(){
    float gamma = 2.2;
    vec3 color = texture(u_texture_0, uv_0).rgb;
    color = pow(color, vec3(gamma));
    color = getLight(color);
    color = pow(color, 1 / vec3(gamma));
    fragColor = vec4(color, 1.0);
}