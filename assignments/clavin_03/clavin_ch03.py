#author: andrew clavin
#date: February Tenth, 2016
#desc: how many songs fit on an ipod

def songsOnIpod(p_capacity, p_bitrate):
    timePerSong = 4*60
    #capacity in gigs so convert to bytes (*2^30) then to bits (*8)
    #bitrate in kbps so multiply by 1000
    return p_capacity * ((2 ** 30) * 8) / (timePerSong * p_bitrate * 1000)

#make some test cases
def main():
    testArray = [[8, 192], [32, 192], [64, 192], [2, 128], [0.5, 128], [100, 128]]
    for case in testArray:
        print("With " + str(case[0]) +
            " gigs sampled at " + str(case[1]) +
            " kbps you can fit approximately " + str(songsOnIpod(case[0], case[1]))
            + " songs.")
        
main()
