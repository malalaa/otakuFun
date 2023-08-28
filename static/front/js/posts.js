var PostsHandler = function(){
    var csrf_token = $("meta[name='csrf-token']").attr("content");
    var editor = new window.wangEditor("#editor");
    editor.config.uploadImgServer = "/post/image/upload";
    editor.config.uploadFileName = "image";
    editor.config.uploadImgHeaders = {
        "X-CRSFToken": csrf_token
    }
    editor.config.uploadImgMaxSize = 1024*1024*5;
    editor.create();
    this.editor = editor;

}

PostsHandler.prototype.listenSubmitEvent = function(){
    $("#submit-btn").on("click", function(event){
        event.preventDefault();
        var title = $("input[name='title']").val();
        var board_id = $("input[name='board_id']").val();
        var content = this.editor.txt.html();
        zlajax.post({
            utl: "/post/publish"
            data: {title, board_id, content},
            success: function(result){
                if(result['code']==200){
                    alert("帖子发表成功");
                }
            }
        });
    });

}

PostsHandler.prototype.run() = function(){}

$(function(){
    var handler = new PostsHandler();
    handler.run();
});