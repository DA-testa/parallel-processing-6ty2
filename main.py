# python3

def parallel_processing(n, m, data):
    output = []
    first_times =[0]*n

    for i in range(m):
        minum_time = min(first_times)
        first_index = first_times.index(minum_time)

        output.append((first_index, minum_time))
        if i<len(data):
            first_times[first_index]+=data[i]
    return output

def main():

    n,m =map(int,input().split())
    data = list(map(int,input().split()))
    


    result = parallel_processing(n,m,data)
    
    # TODO: print out the results, each pair in it's own line

for thread_index, start_time in result:
        print(thread_index, start_time)

if __name__ == "__main__":
    main()
