<script>
	import { browser } from '$app/environment';
	import tokens from '$lib/shared/store/jwt.js';
	import { enhance } from '$app/forms';

	export let data;

	let image = browser ? data.json.profile_photo : null;

	let submitted_image, fileinput;
	submitted_image = image;

	const handleReset = async () => {
		submitted_image = image;
	};

	const onFileSelected = (e) => {
		let image = e.target.files[0];
		let reader = new FileReader();
		reader.readAsDataURL(image);
		reader.onload = (e) => {
			submitted_image = e.target.result;
		};
	};

	const handleSubmit = async () => {
		let success = false;
		let errors;

		let request_form_data = new FormData();
		request_form_data.append('profile_photo', submitted_image);

		
		let request_data = {
			method: 'PATCH',
			headers: {
				Authorization: `Bearer ${tokens.access}`,
                // 'Content-Type': 'multipart/form-data'
			},
			body: request_form_data
		};
		
		for (let entry of request_data.body.entries()) {
			console.log(entry);
		}

		let response = await fetch('http://localhost:8000/auth/api/users/me/', request_data);
		if (response.ok) {
			success = true;
		}

		let resp = await response.json();
		if (success !== true) {
			for (const [key, value] of Object.entries(resp)) {
				console.log(key, value);
			}
		}
	};
</script>

<div
	class="m-10 px-16 rounded-lg bg-gray-200 h-[calc(100%-120px)] overflow-hidden font-bold flex justify-center flex-wrap font-mono items-center py-28"
>
	<div
		class="border-4 h-1/2 w-1/3 border-gray-700 flex justify-center items-center overflow-hidden"
	>
		{#if submitted_image}
			<img src={submitted_image} alt="..." />
		{:else if image}
			<img src={image} alt="..." class="h-full text-xl text-center" />
		{:else}
			<div class="h-full w-full text-xl flex justify-center items-center text-center">
				No Profile Image Set...
			</div>
		{/if}
	</div>

	<form
		method="post"
        use:enhance
		on:submit|preventDefault={handleSubmit}
		enctype="multipart/form-data"
		class="flex w-full justify-center flex-wrap"
	>
		<button
			class="w-2/3 bg-gray-800 text-white py-4 text-xl rounded-l-xl hover:bg-gray-600 mt-5"
			on:click={() => {
				fileinput.click();
			}}
		>
			Choose Image
		</button>
		<input
			style="display:none"
			type="file"
			accept="image/jpeg,image/png,image/gif"
			on:change={(e) => onFileSelected(e)}
			bind:this={fileinput}
		/>

		<button
			on:click={handleReset}
			class="w-1/4 h-20 bg-gray-800 text-white py-4 text-xl rounded-r-xl hover:bg-gray-600 mt-5"
		>
			<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" class="w-full h-full fill-white"
				><path
					d="M463.5 224H472c13.3 0 24-10.7 24-24V72c0-9.7-5.8-18.5-14.8-22.2s-19.3-1.7-26.2 5.2L413.4 96.6c-87.6-86.5-228.7-86.2-315.8 1c-87.5 87.5-87.5 229.3 0 316.8s229.3 87.5 316.8 0c12.5-12.5 12.5-32.8 0-45.3s-32.8-12.5-45.3 0c-62.5 62.5-163.8 62.5-226.3 0s-62.5-163.8 0-226.3c62.2-62.2 162.7-62.5 225.3-1L327 183c-6.9 6.9-8.9 17.2-5.2 26.2s12.5 14.8 22.2 14.8H463.5z"
				/></svg
			>
		</button>

		<button
			type="submit"
			class="w-[91.66%] mt-1 h-20 bg-gray-800 text-white py-4 text-xl rounded-xl hover:bg-gray-600"
		>
			Change Profile Photo
		</button>
	</form>
</div>
