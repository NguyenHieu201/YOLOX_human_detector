input="/home/hieu/hieunm/multicams_human_tracking/videos/input/supermarket/201.mp4"
output="./datasets/supermarket/201_30s.mp4"
ffmpeg -i "$input" -ss 00:00:00 -to 00:00:30 $output

input="/home/hieu/hieunm/multicams_human_tracking/videos/input/supermarket/202.mp4"
output="./datasets/supermarket/202_30s.mp4"
ffmpeg -i "$input" -ss 00:00:00 -to 00:00:30 $output

input="/home/hieu/hieunm/multicams_human_tracking/videos/input/supermarket/203.mp4"
output="./datasets/supermarket/203_30s.mp4"
ffmpeg -i "$input" -ss 00:00:00 -to 00:00:30 $output