public class MainActivity extends Activity {
	private TextView test_tv1;
	private TextView test_tv2;
	private TextView test_tv3;
	private Button button_bt;

	private void findAllView(){
		test_tv1 = (TextView)findViewById(R.id.test_tv1);
		test_tv2 = (TextView)findViewById(R.id.test_tv2);
		test_tv3 = (TextView)findViewById(R.id.test_tv3);
		button_bt = (Button)findViewById(R.id.button_bt);
	}
}