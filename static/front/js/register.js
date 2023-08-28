var RegisterHandler = function(){

}
RegisterHandler.prototype.listenSendCaptchaEvent = function(){
//    选择器
    var callback = function(event){
    var $this = $(this);
    event.preventDefault();
    var email = $("input[name='email']").val();
    var reg = /^\w+((.\w+)|(-\w+))@[A-Za-z0-9]+((.|-)[A-Za-z0-9]+).[A-Za-z0-9]+$/;
    if(!email || !reg.test(email)){
        alert("请输入正确格式的邮箱!");
        return;
    }
    zlajax.get({
        url: "/email/captcha?email="+email,
        success: function (result){
            if(result['code']==200){
                console.log("邮件发送成功！");
                $this.off("click");
                $this.attr("disabled", "disabled");
                var countdown = 60;
                var interval = setInterval(function(){
                    if(countdown>0){
                        $this.text(countdown);
                    }else{
                        $this.text("发送验证码");
                        $this.attr("disabled", false);
                        $this.on("click", callback);
                        clearInterval(interval);
                    }
                    countdown--;
                }, 1000);
            }else{
                var message = result['message'];
                alert(message);
            }
        }
    })
    }
    $("#email-captcha-btn").on("click", callback);
}


RegisterHandler.prototype.listenGraphCaptchaEvent = function(){
    $('#captcha-img').on('click',function(){
    console.log('点击了图形验证码');
    var $this = $(this);
    var src = $this.attr('src');
    //防止一些浏览器在两次url相同时不会更行图形验证码
    let new_src = zlparam.setParam(src,"sign", Math.random())
    $this.attr('src',new_src);
    });
}

RegisterHandler.prototype.listenSubmitEvent = function(){
    $("#submit-btn").on("click", function(event){
    event.preventDefault();
    var email = $("input[name='email']").val();
    var email_captcha = $("input[name='email_captcha']").val();
    var username = $("input[name='username']").val();
    var password = $("input[name='password']").val();
    var repeat_password = $("input[name='repeat_password']").val();
    var graph_captcha = $("input[name='graph_captcha']").val();


    zlajax.post({
        url:"/register",
        data:{
        "email": email,
        "email_captcha":email_captcha,
        "username":username,
        password,
        repeat_password,
        graph_captcha,
        },
        success:function(result){
            if(result['code']==200){
                window.location = "/login";
            }else{
                alert(result['message']);
            }
        }
    })
    });
}


RegisterHandler.prototype.run = function(){
    this.listenSendCaptchaEvent();
    this.listenGraphCaptchaEvent();
    this.listenSubmitEvent();
}

$(function(){
    var handler = new RegisterHandler();
    handler.run();

//会在整个网络全都加载完之后执行这个代码，因为js在头文件而button在body中。
})