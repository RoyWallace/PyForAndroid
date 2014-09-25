import android.content.Context;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.BaseAdapter;
import java.util.ArrayList;
import java.util.List;

/**
 * Created by Administrator on 2014/9/17.
 */
public class CommentAdapter extends BaseAdapter {

    private Context context;

    private List<Object> objectList = new ArrayList<Object>();

    public CommentAdapter(Context context, List<String> commentList){
        this.context = context;
        this.commentList = commentList;
    }

    @Override
    public int getCount() {
        return commentList.size();
    }

    @Override
    public Object getItem(int i) {
        return null;
    }

    @Override
    public long getItemId(int i) {
        return 0;
    }

    @Override
    public View getView(int i, View view, ViewGroup viewGroup) {

        ViewHolder holder = null;
        if(view== null){
            view = LayoutInflater.from(context).inflate(R.layout.item_comment,null);
            holder = new ViewHolder();
            holder.avatarIv = view.findViewById(R.id.avatarIv);
            holder.userNmaeTv = view.findViewById(R.id.userNmaeTv);
            holder.commentTv = view.findViewById(R.id.commentTv);
            view.setTag(holder);
        }else{
            holder = (ViewHolder) view.getTag();
        }
        
        holder.avatarIv.setImageResource();
        
        holder.avatarIv.setOnClickListener(new View.OnClickListener(){
             @Override
            public void onClick(View view){
                
            }
        });
        
        holder.userNmaeTv.setText();
        
        holder.userNmaeTv.setOnClickListener(new View.OnClickListener(){
             @Override
            public void onClick(View view){
                
            }
        });
        
        holder.commentTv.setText();
        
        holder.commentTv.setOnClickListener(new View.OnClickListener(){
             @Override
            public void onClick(View view){
                
            }
        });

        return view;
    }

    private class ViewHolder{
        ImageView avatarIv;

        TextView userNmaeTv;

        TextView commentTv;
    }
}