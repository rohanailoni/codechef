import java.util.*;
import java.io.*;

class Solution{
    static class FastReader{
        BufferedReader br;
        StringTokenizer st;
        public FastReader(){
            br=new BufferedReader(new InputStreamReader(System.in));
        }
        String next(){
            while(st==null || !st.hasMoreTokens()){
                try {
                    st=new StringTokenizer(br.readLine());
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
            return st.nextToken();
        }
        int nextInt(){
            return Integer.parseInt(next());
        }
        long nextLong(){
            return Long.parseLong(next());
        }
        double nextDouble(){
            return Double.parseDouble(next());
        }
        String nextLine(){
            String str="";
            try {
                str=br.readLine().trim();
            } catch (Exception e) {
                e.printStackTrace();
            }
            return str;
        }
    }
    static class FastWriter {
		private final BufferedWriter bw;

		public FastWriter() {
			this.bw = new BufferedWriter(new OutputStreamWriter(System.out));
		}

		public void print(Object object) throws IOException {
			bw.append("" + object);
		}

		public void println(Object object) throws IOException {
			print(object);
			bw.append("\n");
		}

		public void close() throws IOException {
			bw.close();
		}
	}
    static int[] string_to_array(String[] arr){
        int[] ans=new int[arr.length];
        for(int i=0;i<arr.length;i++){
            ans[i]=Integer.parseInt(arr[i]);
        }
        return ans;
    }
    public static void main(String[] args) {
        try {
            FastReader in=new FastReader();
            FastWriter out = new FastWriter();
            int testCases=in.nextInt();
            while(testCases-- > 0){
                // write code here
				int n,k;
				int[] book=string_to_array(in.nextLine().split(" "));
				n=book[0];
				k=book[1];
				int[] arr=new int[n];
				for(int i=0;i<n;i++){
					arr[i]=i+1;
				}
				int pos=1;
				int req=(n*(n+1))/2-k;
				out.println(Arrays.toString(arr));

				for(int i=n-1;i>=1 && req>0;i--){
					if(req>=i){
						req-=i;
						arr[pos]=1;

					}else{
						arr[pos+(i-req)]=1;
						req=0;
					}
				pos+=1;		
				}
				//out.println(Arrays.toString(arr));            
				for(int i:arr)out.print(i+" ");
				out.print("\n");
			}
            out.close();
        } catch (Exception e) {
            System.out.println(e);
			return;
        }
    }
}

