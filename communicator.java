    import org.omg.SendingContext.RunTime;

    import java.io.*;
    import java.math.BigInteger;
    import java.rmi.server.ExportException;
    import java.util.LinkedList;
    import java.util.Map;
    import java.util.StringTokenizer;

    /**
     * Created by noureldin on 25/04/17.
     */
    public class communicator {
        public static LinkedList<point> pairs = new LinkedList<point>();
        public static String prime,message;

        public static void TalkToEncrypt(int m,int n,String message) throws Exception{
            try{
                ProcessBuilder pb = new ProcessBuilder("python","encrypt.py",
                        n + " " + m + " " + message);

                Process pr = pb.start();
                BufferedReader input = new BufferedReader(new InputStreamReader(pr.getInputStream()));
                String line;
                while ((line=input.readLine()) != null)
                    System.err.println(line);
                int exitval = pr.waitFor();
                if(exitval != 0) throw new Exception("failed");
            }
            catch (Exception e){
                System.err.println(e.getMessage());
                throw e;
            }
        }


        public static void main(String[] args) throws Exception{
            TalkToEncrypt(2,3,"10");
        }
    }

    class point{
        String X,Y;
        public point(String X,String Y){
            this.X = X;
            this.Y = Y;
        }
        @Override
        public String toString(){
            return "(" + this.X + " ," + this.Y + ")";
        }
    }
    class IO{
        private BufferedReader br;
        private StringTokenizer st;
        private PrintWriter writer;
        private String inputFile,outputFile;

        public String getNext() throws FileNotFoundException, IOException {
            while(st == null || !st.hasMoreTokens()) st = new StringTokenizer(br.readLine());
            return st.nextToken();
        }

        public String getNextLine() throws FileNotFoundException, IOException{
            return br.readLine().trim();
        }

        public int getNextInt() throws FileNotFoundException, IOException{
            return Integer.parseInt(getNext());
        }
        public long getNextLong() throws FileNotFoundException, IOException{
            return Long.parseLong(getNext());
        }

        public void print(double x,int num_digits) throws  IOException{
            writer.printf("%." + num_digits + "f" ,x);
        }
        public void println(double x,int num_digits) throws  IOException{
            writer.printf("%." + num_digits + "f\n" ,x);
        }
        public void print(Object o) throws  IOException{
            writer.print(o.toString());
        }

        public void println(Object o) throws  IOException{
            writer.println(o.toString());
        }
        public IO(String x,String y) throws FileNotFoundException, IOException{
            inputFile = x;
            outputFile = y;
            if(x != null) br = new BufferedReader(new FileReader(inputFile));
            else br = new BufferedReader(new InputStreamReader(System.in));
            if(y != null) writer = new PrintWriter(new BufferedWriter(new FileWriter(outputFile)));
            else writer = new PrintWriter(new OutputStreamWriter(System.out));
        }

        protected void close() throws IOException{
            br.close();
            writer.close();
        }
    }


