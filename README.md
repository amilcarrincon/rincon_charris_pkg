# rincon_charris_pkg
Este proyecto utiliza el dataset r2b_robotarm del R2B Dataset 2024 de NVIDIA (https://catalog.ngc.nvidia.com/orgs/nvidia/teams/isaac/resources/r2bdataset2024), que contiene datos sensoriales y de control de un brazo robótico. Me llamó la atención este dataset porque permite trabajar con percepción visual y control de actuadores en un entorno simulado que se aproxima a la realidad, lo cual resulta ideal para comenzar a explorar conceptos fundamentales de ROS 2.

Para usar el dataset se de deben corre los siguientes pasos: 

paso 1: Instalar el cliente de NGC:
  wget --content-disposition https://ngc.nvidia.com/downloads/ngccli_linux.zip
  unzip ngccli_linux.zip
  chmod u+x ngc-cli/ngc
  
paso 2: Descargar el dataset:
  ./ngc-cli/ngc registry resource download-version "nvidia/isaac/r2bdataset2024:1"
  
paso 3: Ubicar la carpeta r2bdataset2024_v1/ en el mismo nivel que rincon_charris_pkg/
