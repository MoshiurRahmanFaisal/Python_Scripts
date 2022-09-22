#Trim Video

from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
ffmpeg_extract_subclip("3.mp4", 80, 82, targetname="test1.mp4")

# #Merge_video
# from moviepy.editor import VideoFileClip, concatenate_videoclips


# clip_1 = VideoFileClip("3.mp4")
# clip_2 = VideoFileClip("test.mp4")
# final_clip = concatenate_videoclips([clip_1,clip_2])
# final_clip.write_videofile("final.mp4")

