class ShrinkersController < ApplicationController
  # Just for testing it with postman. Remove it once done.
  protect_from_forgery except: :shrink


  def shrink
    puts params
    original_url = params[:original_url]
    print original_url
  end

end
