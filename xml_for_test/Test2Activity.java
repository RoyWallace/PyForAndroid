public class Test2Activity extends Activity {
	private TextView test_tv1;
	private TextView test_tv2;
	private TextView test_tv3;
	private Button button_bt;
	private ScrollView scroll_view;

	private void findAllView(){
		test_tv1 = (TextView)findViewById(R.id.test_tv1);
		test_tv2 = (TextView)findViewById(R.id.test_tv2);
		test_tv3 = (TextView)findViewById(R.id.test_tv3);
		button_bt = (Button)findViewById(R.id.button_bt);
		scroll_view = (ScrollView)findViewById(R.id.scroll_view);
	}
}