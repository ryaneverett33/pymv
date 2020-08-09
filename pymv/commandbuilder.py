from pymv.fmap import fmap
from pymv.codecinfo import codecinfo
from pymv.bitrateinfo import bitrateinfo
from pymv.metadatainfo import metadatainfo

class commandbuilder:
    inputs = None
    outputs = None
    mapping = None
    codec_info = None
    bitrate_info = None
    metadata_info = None
    input_info = None
    video_info = None
    audio_info = None
    subtitle_info = None
    videooptions = None
    otheroptions = None

    def __init__(self):
        self.inputs = []
        self.outputs = []
        self.codec_info = codecinfo()
        self.bitrate_info = bitrateinfo()
        self.metadata_info = metadatainfo()
        self.otheroptions = list()

    def get_ffmpeg(self):
        return "ffmpeg"

    def get_ffprobe(self):
        return "ffprobe"

    def get_arguments(self):
        arguments = []
        # assemble inputs
        if self.inputs is not None:
            for filename in self.inputs:
                arguments.append('-i')
                arguments.append("{0}".format(filename))
        else:
            raise Exception('No inputs specified!')

        # assemble mappings
        if self.mapping is not None:
            if isinstance(self.mapping, fmap):
                arguments.extend(self.mapping.to_args())
            else:
                for maps in self.mapping:
                    arguments.extend(maps.to_args())

        # assemble codecs
        if self.codec_info is not None:
            codec_args = self.codec_info.to_args()
            arguments.extend(codec_args)
        
        # assemble bitrates
        if self.bitrate_info is not None:
            bitrate_args = self.bitrate_info.to_args()
            arguments.extend(bitrate_args)

        # assemble metadata
        if self.metadata_info is not None:
            metadata_args = self.metadata_info.to_args()
            arguments.extend(metadata_args)

        # assemble other options
        if len(self.otheroptions) != 0:
            arguments.extend(self.otheroptions)

        # assemble outputs
        if self.outputs is not None:
            for filename in self.outputs:
                arguments.append("{0}".format(filename))
        else:
            raise Exception('No outputs specified!')
        return arguments